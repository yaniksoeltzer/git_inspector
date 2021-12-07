from git import Commit
import logging


class CommitResolveError(Exception):
    pass


def get_tracked_heads(repo):
    return list(filter(
        lambda head: head.tracking_branch() is not None,
        repo.heads
    ))


def get_untracked_heads(repo):
    return list(filter(
        lambda head: head.tracking_branch() is None,
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


def is_ancestors_of(ancestor: Commit, commit: Commit):
    return depth_search_commit([commit], [], ancestor) is not None


def depth_search_commit(fringe: iter, visited: list, goal_node: Commit, cur_dept=0):
    if len(fringe) == 0:
        return None
    if cur_dept >= 100:
        logging.debug(f"max depth reached for is_ancestors_of of {goal_node.repo.working_dir}")
        return None
    if goal_node in fringe:
        return 0
    new_fringe = []
    for fring in fringe:
        f_parents = fring.parents
        new_fringe.extend(f_parents)
    new_fringe = [x for x in new_fringe if x not in visited]
    visited += fringe
    try:
        dept = depth_search_commit(new_fringe, visited, goal_node, cur_dept + 1)
    except ValueError as e:
        # A value error like the following is risen if the remote can not be resolved any further
        # ValueError: SHA b'7692881d2a61a4ba47eeef5d7827c0d2cb896def' could not be resolved, git returned:
        # b'7692881d2a61a4ba47eeef5d7827c0d2cb896def missing
        raise CommitResolveError(e)
    if dept is not None:
        return dept + 1
    return None
