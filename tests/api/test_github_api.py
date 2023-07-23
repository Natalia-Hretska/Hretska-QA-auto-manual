import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
   
    assert r["total_count"] == 42
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0



@pytest.mark.api   
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


@pytest.mark.api
def test_emojis_exists(github_api):
    r = github_api.get_all_emojis()
    
#    assert r['zombie_woman'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f9df-2640.png?v8'
    assert isinstance(r, dict)
    assert len(r) > 0

@pytest.mark.api
def test_get_commits_sucsessful(github_api): 
    r = github_api.get_commits("natalia-hretska", "hretska-qa-auto-manual")
    
    assert isinstance(r, list)
    assert len(r) > 0

@pytest.mark.api
def test_commits_invalid_owner(github_api):
    r = github_api.get_commits("hretska", "hretska-qa-auto-manual")   

    assert isinstance(r, dict)
    assert "message" in r
    assert r["message"] == "Not Found"

@pytest.mark.api
def test_get_commits_invalid_repo(github_api):
    r = github_api.get_commits("natalia-hretska","pushka")

    assert isinstance(r, dict)
    assert "message" in r
    assert r["message"] == "Not Found"

@pytest.mark.api
def test_commit_structure(github_api):
    r = github_api.get_commits("natalia-hretska", "hretska-qa-auto-manual")
    
    for commit in r:
        assert "sha" in commit
        assert "commit" in commit
        assert "author" in commit["commit"]
        assert "message" in commit["commit"]

    
   