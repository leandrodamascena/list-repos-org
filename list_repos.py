from github import Github

access_token = "TOKEN"
organization_name = "experimentos-k8s"


# WARNING: Don't commit this code with the access_token code
github = Github(access_token)

# Uncomment this line if using GH Enterprise and set the custom domain
#github = Github(base_url="https://{url}/api/v3", login_or_token=access_token)

org = github.get_organization(organization_name)

# Then play with your Github objects:
# List
team_name = ""
for repo in org.get_repos():
    print("##")
    print(f'Name: {repo.name}')
    print(f'URL: {repo.url}')
    print(f'Teams:')
    for team in repo.get_teams():
        print(f'  TeamName: {team.name}')
        print(f'  TeamPermission: {team.permission}')
        print(f'  --')
    print(f'Owner: {repo.owner.login}')
    print(f'Created at: {repo.created_at}')
    print(f'Updated at: {repo.updated_at}')
    print(f'Last push: {repo.pushed_at}')
