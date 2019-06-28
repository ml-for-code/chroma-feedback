import requests
import src.provider.appveyor.core as appveyor
import src.provider.circle.core as circle
import src.provider.github.core as github
import src.provider.gitlab.core as gitlab
import src.provider.jenkins.core as jenkins
import src.provider.teamcity.core as teamcity
import src.provider.travis.core as travis


def process(args):
	data = []
	for provider in args.provider:
		if args.slug:
			for slug in args.slug:
				data.extend(fetch(provider, args.host, slug, args.auth))
		elif args.auth:
			data.extend(fetch(provider, args.host, None, args.auth))
	return data


def fetch(provider, host, slug, auth):
	try:
		if provider == 'appveyor':
			return appveyor.fetch(host, slug, auth)
		if provider == 'circle':
			return circle.fetch(host, slug, auth)
		if provider == 'github':
			return github.fetch(host, slug, auth)
		if provider == 'gitlab':
			return gitlab.fetch(host, slug, auth)
		if provider == 'jenkins':
			return jenkins.fetch(host, slug)
		if provider == 'teamcity':
			return teamcity.fetch(host, slug, auth)
		if provider == 'travis':
			return travis.fetch(host, slug)
	except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema):
		pass
	return []
