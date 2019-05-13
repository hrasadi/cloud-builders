import os
import sys

ucl_version = 'v1'

def generate_ucl_path(repo, branch, commit_hash):
  # TODO(hasaad): identify 
  ucl_path = ('ucl://github/' + repo + '/' + branch + '/' + commit_hash +
              '?version=' + ucl_version)
  return ucl_path


def generate_ucl():
  if os.environ.get('REPO_NAME') != None:
    # By existance of this env var we assume that workspace was cloned from a 
    # Github repo
    # TODO(hasaadi): identify the repo type (Github, Gitlab, etc.)
    # TODO(hasaadi): convert GCB repo name to UCL org+repo format
    repo = os.environ.get('REPO_NAME')
    branch = os.environ.get('BRANCH_NAME')
    commit_hash = os.environ.get('SHORT_SHA')
    ucl_tag = generate_ucl_path(repo, branch, commit_hash)

    with open('__UCL__', 'w') as tag_file:
      tag_file.write(ucl_tag)
  else:
    # Not a checked-in source. Abort.
    sys.exit(0) 


if __name__ == '__main__':
  generate_ucl();
