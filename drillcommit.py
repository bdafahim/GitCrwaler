from pydriller import Repository
from datetime import datetime
from pydriller.metrics.process.change_set import ChangeSet
from pydriller.metrics.process.code_churn import CodeChurn

repo = 'https://github.com/bdafahim/DatingApp-SPA.git'

#traverse all the commits
print('traverse all the commits')
for commit in Repository(repo).traverse_commits():
    print('Hash {}, author {} committed by {} in date {}'.format(commit.hash, commit.author.name, commit.committer.name, commit.committer_date))

    
# Analyze single commit
singleCommit = Repository(repo, single='40ce97f9c9f39f884cd4aa8cd4450ba6ad1f1bd1').traverse_commits()
print('Single commit')
for info in singleCommit:
    print(info.author_date, info.branches, info.files, info.hash, info.project_name, info.project_path, info.parents, info.insertions, info.lines, info.deletions, info.modified_files, info.msg)


# Since 24/03/2020
commits = Repository(repo, since=datetime(2020, 3, 24, 17, 0, 0)).traverse_commits()
print('Since 24/03/2020')
for commit in commits:
    print('Hash {}, author {}'.format(commit.hash, commit.author.name))



# Between 2 dates
dt1 = datetime(2020, 3, 24, 17, 0, 0)
dt2 = datetime(2020, 3, 31, 17, 59, 0)
print('Between 2 dates')
for commit in Repository(repo, since=dt1, to=dt2).traverse_commits():
    print('Hash {}, author {}'.format(commit.hash, commit.author.name))



# Only commits in master
Repository(repo, only_in_branch='master').traverse_commits()

# Only commits in branch1 and no merges
Repository(repo, only_in_branch='master', only_no_merge=True).traverse_commits()

# Only commits of author "ishepard" (yeah, that's me)
Repository(repo, only_authors=['bdafahim']).traverse_commits()

# Only these 3 commits
Repository(repo, only_commits=['hash1', 'hash2', 'hash3']).traverse_commits()

# Only commits that modified a html file
commits = Repository(repo, only_modifications_with_file_types=['.html']).traverse_commits()
print(' Only commits that modified a html file')
for commit in commits:
     print('Hash {}, author {}'.format(commit.hash, commit.author.name))


#Modified files

print('Modified Files')
for commit in Repository(repo).traverse_commits():
    for m in commit.modified_files:
        print(
            "Author {}".format(commit.author.name),
            " modified {}".format(m.filename),
            " with a change type of {}".format(m.change_type.name),
            " and the complexity is {}".format(m.complexity)
        )


#Process Metrics
metric = ChangeSet(path_to_repo=repo,
                   from_commit='3ae5e9b938d2119b3070a704bde5a0e01d9d1cb8',
                   to_commit='40ce97f9c9f39f884cd4aa8cd4450ba6ad1f1bd1')

maximum = metric.max()
average = metric.avg()
print('Change set')
print('Maximum number of files committed together: {}'.format(maximum))
print('Average number of files committed together: {}'.format(average))

'''
metric = CodeChurn(path_to_repo=repo,
                   from_commit='bf140738d2a8d822feb30a3d3e3a46345653f41d',
                   to_commit='40ce97f9c9f39f884cd4aa8cd4450ba6ad1f1bd1')
files_count = metric.count()
files_max = metric.max()
files_avg = metric.avg()
print('code churn')
print('Total code churn for each file: {}'.format(files_count))
print('Maximum code churn for each file: {}'.format(files_max))
print('Average code churn for each file: {}'.format(files_avg))
'''



# Contributors Count

from pydriller.metrics.process.contributors_count import ContributorsCount
metric = ContributorsCount(path_to_repo=repo,
                           from_commit='bf140738d2a8d822feb30a3d3e3a46345653f41d',
                           to_commit='40ce97f9c9f39f884cd4aa8cd4450ba6ad1f1bd1')

print('Contributors Count')
count = metric.count()
minor = metric.count_minor()
print('Number of contributors per file: {}'.format(count))
print('Number of "minor" contributors per file: {}'.format(minor))


# Lines Count

from pydriller.metrics.process.lines_count import LinesCount
metric = LinesCount(path_to_repo=repo,
                    from_commit='bf140738d2a8d822feb30a3d3e3a46345653f41d',
                    to_commit='40ce97f9c9f39f884cd4aa8cd4450ba6ad1f1bd1')

added_count = metric.count_added()
added_max = metric.max_added()
added_avg = metric.avg_added()
print('Lines Count')
print('Total lines added per file: {}'.format(added_count))
print('Maximum lines added per file: {}'.format(added_max))
print('Average lines added per file: {}'.format(added_avg))










# A Commit object has all the information of a Git commit, and much more. More specifically:

''' hash (str): hash of the commit

msg (str): commit message

author (Developer): commit author (name, email)

committer (Developer): commit committer (name, email)

author_date (datetime): authored date

author_timezone (int): author timezone (expressed in seconds from epoch)

committer_date (datetime): commit date

committer_timezone (int): commit timezone (expressed in seconds from epoch)

branches (List[str]): List of branches that contain this commit

in_main_branch (Bool): True if the commit is in the main branch

merge (Bool): True if the commit is a merge commit

modified_files (List[ModifiedFile]): list of modified files in the commit (see ModifiedFile)

parents (List[str]): list of the commit parents

project_name (str): project name

project_path (str): project path

deletions (int): number of deleted lines in the commit (as shown from –shortstat).

insertions (int): number of added lines in the commit (as shown from –shortstat).

lines (int): total number of added + deleted lines in the commit (as shown from –shortstat).

files (int): number of files changed in the commit (as shown from –shortstat).

dmm_unit_size (float): DMM metric value for the unit size property.

dmm_unit_complexity (float): DMM metric value for the unit complexity property.

dmm_unit_interfacing (float): DMM metric value for the unit interfacing property.'''
