#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -p 本地git项目地址  -v tag号  -r 需要执行的操作
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", default='D:\Work\git\creep', help='Local git repo address')
parser.add_argument("-v", "--version", default='1.0.0', help='tag version')
parser.add_argument("-r", "--run", required=True, help='the instruction to run')
args = parser.parse_args()
print('git repo path: %s' % args.path)
print('tag name: %s' % args.version)
print('command to run: %s' % args.run)

# 项目路径
path = args.path

# 要打的基线名
version = args.version

# 需要执行的操作
run = args.run

# 需要替换的文件名
replace_file = 'Server-2018-08-29.log'

# 获取当前路径
home = os.getcwd()

# 移动盘符到指定目录
os.chdir(path)


def auto():
    pre()
    pull()    
    del_loc_branch()
    del_local_tag()
    del_ori_tag()
    new_branch()
    replace()
    commit()
    tag()
    tag_push()


def replace():
    # 删除配置文件
    # os.remove("target" + os.sep + "creep-0.0.1-SNAPSHOT.jar.original")
    # 替换需要替换的配置文件
    with open(path + os.sep + replace_file, 'w+', encoding='UTF-8') as file_open:
        with open(home + os.sep + replace_file, 'r', encoding='UTF-8') as file_new:
            for line in file_new:
                file_open.write(line)
    # print(os.getcwd())
    print("==================================")
    print(">>>>replace done!")
    print("==================================")


def run_bash(command):
    p = os.popen(command)
    print("==================================")
    print(p.read())
    print("==================================")
    p.close()


def tags_list():
    run_bash('git tag -l')


def new_branch():
    run_bash('git checkout -b ' + version)

def pull():
    run_bash('git pull')
    
def pre():
    run_bash('git add -A')
    run_bash('git commit -m"test"')
    run_bash('git checkout master')
    
    
def tag():
    run_bash('git tag ' + version)


def commit():
    run_bash('git add src/*')
    run_bash('git commit -m":smile:' + version + '"')


# 推送tag
def tag_push():
    run_bash('git push --tags')


# 推送本地更新
def push():
    run_bash('git push')


def del_loc_branch():
    run_bash('git branch -D ' + version)


# 删除远程branch
def del_ori_branch():
    run_bash('git push origin --delete ' + version)


# 删除远程tag
def del_ori_tag():
    run_bash('git push origin --delete tag ' + version)


# 删除本地tag
def del_local_tag():
    run_bash('git tag -d ' + version)


magic_list = {
    # 一条龙
    "auto": auto,
    # 替换需要替换的文件
    "replace": replace,
    # 显示本地tag
    "show": tags_list,
    # 删除远程tag
    "d_ori": del_ori_tag,
    # 删除本地tag
    "d_local": del_local_tag,
    # 推送tag
    "push_tag": tag_push,
    # tag
    "tag": tag,
    # commit
    "commit": commit,
    # 推送本地更新
    "push": push
}


def magic(command):
    try:
        return magic_list.get(command)
    except Exception as err:
        print(err)


magic(run)()
