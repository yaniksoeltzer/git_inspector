import os

from git import Commit, Remote
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
    return head.name == 'master' or head.name == 'main'


def get_master_branch(repo):
    for head in repo.heads:
        if is_master_branch(head):
            return head
    return None


def get_non_master_branches(repo):
    return list(filter(lambda x: not is_master_branch(x), repo.heads))


def is_ancestors_of(ancestor: Commit, commit: Commit):
    return depth_search_commit([commit], [], ancestor) is not None


def depth_search_commit(fringe: iter, visited: list, goal_node: Commit):
    cur_dept = 0
    while True:
        if len(fringe) == 0:
            return None
        if goal_node in fringe:
            return cur_dept
        new_fringe = []
        for fring in fringe:
            f_parents = fring.parents
            new_fringe.extend(f_parents)
        new_fringe = [x for x in new_fringe if x not in visited]
        visited += fringe
        fringe = new_fringe
        cur_dept += 1


def remote_is_gone(remote: Remote):
    for url in remote.urls:
        if url.startswith("file://"):
            if not os.path.exists(url):
                return True
        elif url.startswith("/"):
            if not os.path.exists(url):
                return True
    return False

