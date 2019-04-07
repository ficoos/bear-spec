#!/usr/bin/bash

# this is script is meant to be run by cron to synchronize the rpm with
# the upstream version with minimal interaction from a human

cd $(dirname "$0")
remote=https://github.com/rizsotto/Bear.git
src_dir=Bear
if [ ! -d "$src_dir" ]; then
	git clone "$remote" "$src_dir"
fi

pushd "$src_dir"
git pull --tags
latest_tag=$(git describe --abbrev=0)
popd
current_tag=$(git describe --abbrev=0)
if [ "$latest_tag" != "$current_tag" ]; then
    echo "Updating to $latest_tag"
	sed -i -e "s/\(Version:\s\+\)\(\(\w\|\.\)\+\)/\1${latest_tag}/" bear.spec
	git rm "${current_tag}.tar.gz"
	wget "https://github.com/rizsotto/Bear/archive/${latest_tag}.tar.gz"
	git add "${latest_tag}.tar.gz"
	git ci -a -m "Update to version ${latest_tag}"
	git tag -a -m "${latest_tag}" "${latest_tag}"
	git push origin
fi
