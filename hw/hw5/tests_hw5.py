from hashlib import sha1
import numpy as np
import pandas as pd
import re

def hasher(solution):
    print(solution)
    return sha1(solution.encode("utf8")).hexdigest()

def ex1_2_1(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "b9bb31a81074b54e4b37fa208a318bc3d30148ad"
        else False
    )

def ex1_2_2(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "f542db682aa0a9e8e9e8c9a0b3b1a53ffa644ec1"
        else False
    )

def ex1_4_1(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "e8dc057d3346e56aed7cf252185dbe1fa6454411"
        else False
    )

def ex1_4_2(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "856b62aa687c0aa2b0deb2980b3dd887b3c93ff8"
        else False
    )

def ex1_4_3(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "9588c3fcb43fc86f5ac79164cedf59e8e7b9e7ec"
        else False
    )

def ex1_4_4(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "fbccebab4a05483ba1b7ce5c12688ac8f69ec024"
        else False
    )

def ex1_4_5(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "fa5e0ec83bf351a6ad628a5f040cfd01306d1e7d"
        else False
    )

def ex1_4_6(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "ee141dfe56a3bf909677adb103e9afeed9b7bcb4"
        else False
    )



def run_all_autograded_tests(tests, results):
    with open("lab1.ipynb", encoding="utf-8") as f:
        total_autogrades = re.findall("rubric={autograde:(\d).*}", f.read())
    print(f"Autograded questions passed: {sum(results)} / {len(total_autogrades)}")
    print(
        f" Autograded points achieved: {sum([int(digit) for r, digit in zip(results, total_autogrades) if r])} / {sum([int(digit) for digit in total_autogrades])}"
    )
    if sum(results) < len(total_autogrades):
        print("")
        [
            print(f"FAILED: {test}")
            for (test, result) in zip(tests, results)
            if not result
        ]
