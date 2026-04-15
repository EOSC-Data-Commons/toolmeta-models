VERSION = $(shell grep '^version' pyproject.toml | head -1 | cut -d '"' -f2)
version:
	@echo "Current version: v$(VERSION)"

bump:
	@echo "Bumping version from v$(VERSION) to v$(shell uv version --bump patch --dry-run)"
	uv version --bump patch
	uv lock
	git commit -am "Bump version to v"$$(grep '^version' pyproject.toml | head -1 | cut -d '"' -f2)
	git push

git-tag:
	@echo "Tagging version v$(VERSION)"
	@git diff --quiet || (echo "ERROR: Working tree not clean"; exit 1)
	@git tag -a v$(VERSION) -m "Release v$(VERSION)"

git-push-tag:
	@git push origin v$(VERSION)

release: git-tag git-push-tag
	@echo "Released version v$(VERSION)"

