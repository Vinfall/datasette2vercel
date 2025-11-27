# datasette2vercel

[![Test][test-badge]][test-ci]
[![License][license-badge]][license]

Datasette plugin to deploy on [Vercel][vercel], forked from [datasette-publish-vercel][datasette-publish-vercel].

## Install

> [!NOTE]
> As this plugin registers `publish vercel` command just like datasette-publish-vercel, remember to uninstall that first before installation.
> `datasette uninstall datasette-publish-vercel`

```sh
# build wheel
git clone https://github.com/Vinfall/datasette2vercel
cd datasette2vercel
# remove uv prefix if you don't like it
uv pip install .[dev]
python3 -m build
# install from dist
datasette install dist/datasette2vercel-*-py3-none-any.whl
```

## Usage

```sh
# install vercel-cli, https://vercel.com/download
vercel login

# publish mydb database to myproj project on Vercel
datasette publish vercel mydb.db --project=myproj
```

### Other options

- `--no-prod` deploys to the project without updating the "production" URL alias to point to that new deployment. Without that option all deploys go directly to production.
- `--debug` enables the Vercel CLI debug output.
- `--token` allows you to pass a Now authentication token, rather than needing to first run `now login` to configure the tool. Tokens can be created in the Vercel web dashboard under Account Settings -> Tokens.
- `--public` runs `vercel --public` to publish the application source code at `/_src` and make recent logs visible at `/_logs`
- `--generate-dir` - by default this tool generates a new Vercel app in a temporary directory, deploys it and then deletes the directory. Use `--generate-dir=my-app` to output the generated application files to a new directory of your choice instead. You can then deploy it by running `vercel` in that directory.
- `--setting default_page_size 10` - use this to set Datasette settings, as described in [the documentation](https://docs.datasette.io/en/stable/settings.html). This is a replacement for the unsupported `--extra-options` option.

### Full help

> [!WARNING]
> Some of these options are not yet implemented by this plugin.

In particular, the followings do not yet work:

- `--extra-options` - use `--setting` described above instead.
- `--plugin-secret`
- `--version-note`

```sh
$ datasette publish vercel --help

Usage: datasette publish vercel [OPTIONS] [FILES]...

  Publish to https://vercel.com/.

Options:
  -m, --metadata FILENAME         Path to JSON/YAML file containing metadata to publish
  --extra-options TEXT            Extra options to pass to datasette serve
  --branch TEXT                   Install datasette from a GitHub branch e.g. main
  --template-dir DIRECTORY        Path to directory containing custom templates
  --plugins-dir DIRECTORY         Path to directory containing custom plugins
  --static MOUNT:DIRECTORY        Serve static files from this directory at /MOUNT/...
  --install TEXT                  Additional packages (e.g. plugins) to install
  --plugin-secret <TEXT TEXT TEXT>...
                                  Secrets to pass to plugins, e.g. --plugin-secret
                                  datasette-auth-github client_id xxx
  --version-note TEXT             Additional note to show on /-/versions
  --secret TEXT                   Secret used for signing secure values, such as signed
                                  cookies
  --title TEXT                    Title for metadata
  --license TEXT                  License label for metadata
  --license_url TEXT              License URL for metadata
  --source TEXT                   Source label for metadata
  --source_url TEXT               Source URL for metadata
  --about TEXT                    About label for metadata
  --about_url TEXT                About URL for metadata
  --token TEXT                    Auth token to use for deploy
  --project PROJECT               Vercel project name to use  [required]
  --scope TEXT                    Optional Vercel scope (e.g. a team name)
  --no-prod                       Don't deploy directly to production
  --debug                         Enable Vercel CLI debug output
  --public                        Publish source with Vercel CLI --public
  --generate-dir DIRECTORY        Output generated application files and stop without
                                  deploying
  --generate-vercel-json          Output generated vercel.json file and stop without
                                  deploying
  --vercel-json FILENAME          Custom vercel.json file to use instead of generating
                                  one
  --setting SETTING...            Setting, see docs.datasette.io/en/stable/settings.html
  --crossdb                       Enable cross-database SQL queries
  --help                          Show this message and exit.
```

## Using custom `vercel.json`

If you want to add additional redirects or similar to your Vercel configuration you may want to provide a custom `vercel.json` file.

To do this, first generate a configuration file (without running a deploy) using the `--generate-vercel-json` option:

```sh
datasette publish vercel my-database.db \
  --project=my-database \
  --generate-vercel-json > vercel.json
```

You can now edit the `vercel.json` file that this creates to add your custom options.

Then run the deploy using:

```sh
datasette publish vercel my-database.db \
  --project=my-database \
  --vercel-json=vercel.json
```

## Setting `DATASETTE_SECRET`

Datasette uses [a secret string](https://docs.datasette.io/en/stable/settings.html#configuring-the-secret) for purposes such as signing authentication cookies. This secret is reset when the server restarts, which will sign out any users who are authenticated using a signed cookie.

You can avoid this by generating a `DATASETTE_SECRET` secret string and setting that as a [Vercel environment variable](https://vercel.com/docs/concepts/projects/environment-variables). If you do this the secret will stay consistent and your users will not be signed out.

[test-badge]: https://github.com/Vinfall/datasette2vercel/workflows/Test/badge.svg
[test-ci]: https://github.com/Vinfall/datasette2vercel/actions/workflows/test.yml?query=workflow%3ATest
[license-badge]: https://img.shields.io/badge/license-Apache%202.0-blue.svg
[license]: https://github.com/Vinfall/datasette2vercel/blob/main/LICENSE
[vercel]: https://vercel.com/
[datasette-publish-vercel]: https://github.com/simonw/datasette-publish-vercel
