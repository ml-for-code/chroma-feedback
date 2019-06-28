import os
import pytest
import src.provider.github.core as github

def test_fetch_slug():
	if 'GITHUB_TOKEN' in os.environ:
		result = github.fetch(None, 'redaxmedia/chroma-feedback', os.environ['GITHUB_TOKEN'])
		assert result[0]['provider'] == 'github'
		assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('GITHUB_TOKEN not defined')


def test_fetch_invalid():
	result = github.fetch(None, None, None)
	assert result == []
