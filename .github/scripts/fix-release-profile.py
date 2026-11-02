#!/usr/bin/env python3
"""
Run by generate.yml right after openapi-generator regenerates pom.xml.

openapi-generator's java template has no config option for custom Maven profiles or
plugins, so every regeneration resets the release profile to the generator's own default
(id "sign-artifacts", gpg-sign only, no deploy plugin) — wiping out the real one. This
reapplies it: renames the profile id to "release" and adds central-publishing-maven-plugin
so `mvn deploy -P release` (see .github/workflows/publish.yml) actually reaches Maven
Central instead of just signing artifacts nobody uploads anywhere.

Exact string match on purpose: if openapi-generator's default block ever changes shape
(version bump, template change), this fails loudly instead of silently doing nothing and
leaving publish.yml broken again the way it was before — see the postmortem in
docs/sdk/RELEASING.md.

central-publishing-maven-plugin is pinned to 0.12.0, not latest-at-the-time: versions before
0.12.0 bundle Maven 3.10's leftover staging metadata (maven-metadata-local.xml,
_remote.repositories) into the upload, which Central's validator rejects with "Bundle has
content that does NOT have a .pom file" — a real deploy failure we hit, not hypothetical.
Don't downgrade without checking that bug is still fixed in whatever version you pick.
"""
import pathlib
import sys

POM = pathlib.Path("pom.xml")

OLD = """    <profiles>
        <profile>
            <id>sign-artifacts</id>
            <build>
                <plugins>
                    <plugin>
                        <groupId>org.apache.maven.plugins</groupId>
                        <artifactId>maven-gpg-plugin</artifactId>
                        <version>3.2.1</version>
                        <executions>
                            <execution>
                                <id>sign-artifacts</id>
                                <phase>verify</phase>
                                <goals>
                                    <goal>sign</goal>
                                </goals>
                            </execution>
                        </executions>
                    </plugin>
                </plugins>
            </build>
        </profile>
    </profiles>"""

NEW = """    <profiles>
        <profile>
            <id>release</id>
            <build>
                <plugins>
                    <plugin>
                        <groupId>org.apache.maven.plugins</groupId>
                        <artifactId>maven-gpg-plugin</artifactId>
                        <version>3.2.1</version>
                        <executions>
                            <execution>
                                <id>sign-artifacts</id>
                                <phase>verify</phase>
                                <goals>
                                    <goal>sign</goal>
                                </goals>
                            </execution>
                        </executions>
                    </plugin>
                    <plugin>
                        <groupId>org.sonatype.central</groupId>
                        <artifactId>central-publishing-maven-plugin</artifactId>
                        <version>0.12.0</version>
                        <extensions>true</extensions>
                        <configuration>
                            <publishingServerId>central</publishingServerId>
                            <autoPublish>true</autoPublish>
                        </configuration>
                    </plugin>
                </plugins>
            </build>
        </profile>
    </profiles>"""


def main():
    text = POM.read_text()

    if NEW in text:
        print("pom.xml already has the release profile — nothing to do.")
        return

    if OLD not in text:
        sys.exit(
            "fix-release-profile.py: expected generator-default profile block not found "
            "in pom.xml (and the release profile isn't there either). openapi-generator's "
            "output shape probably changed — update OLD/NEW in this script by hand."
        )

    POM.write_text(text.replace(OLD, NEW))
    print("pom.xml release profile patched.")


if __name__ == "__main__":
    main()
