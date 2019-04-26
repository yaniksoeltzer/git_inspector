
def get_tracked_heads(repo):
    return list(filter(
        lambda head: head.tracking_branch() is not None,
        repo.heads
    ))


def compare_commits(commit_1, commit_2):
    if commit_1.hexsha == commit_2.hexsha:
        return 0
    com_1_parent_hex = [p.hexsha for p in commit_1.parents]
    if commit_2.hexsha in com_1_parent_hex:
        return 1
    com_2_parent_hex = [p.hexsha for p in commit_2.parents]
    if commit_1.hexsha in com_2_parent_hex:
        return -1
    return None




def filter_dirty_repos(repos):
    dirty_repos = filter(lambda x: x.is_dirty(), repos)
    return list(dirty_repos)
