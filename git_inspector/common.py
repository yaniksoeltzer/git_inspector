
def get_tracked_heads(repo):
    return list(filter(
        lambda head: head.tracking_branch() is not None,
        repo.heads
    ))


def is_master_branch(head):
    return head.name == 'master'


def get_master_branch(repo):
    for head in repo.heads:
        if is_master_branch(head):
            return head
    return None


def get_non_master_branches(repo):
    return list(filter(lambda x: not is_master_branch(x), repo.heads))


def compare_commits(commit_1, commit_2):
    """
    shows the relation between commit_1 and commit_2
    like doing commit_1 - commit_2
    a positive return value implies that commit_2 is a parent of commit_1
        aka. initial <-- ... <-- commit_2 <-- ... <-- commit_1
    a negative return value implies that commit_1 is a parent of commit_2
        aka. initial <-- ... <-- commit_1 <-- ... <-- commit_2
    returns zero if commits are equal,
    returns None, if neither one commit is the parent of the other.
    """
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
