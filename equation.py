# 描述：一些公式
# 作者：Jelly Lemon

import numpy as np


def objection_1(S, U):
    """
    目标函数 1

    :param S:相似度矩阵
    :param U:预测结果概率矩阵
    :return:目标函数值
    """
    n_sample = len(U)
    sum = 0
    for i in range(n_sample):
        for j in range(n_sample):
            sum += S[i][j] * np.linalg.norm(U[i] - U[j])
    return sum


def objection_2(n_cluster, R, U, Q):
    """
    目标函数 2

    :param n_cluster:聚类器数量
    :param R:聚类结果矩阵
    :param U:预测结果概率矩阵
    :param Q:聚类质心矩阵
    :return:
    """
    n_sample = len(U)
    sum = 0
    for i in range(n_sample):
        for j in range(n_cluster):
            sum += R[i][j] * np.linalg.norm(U[i] - Q[j])
    return sum


def gaussian(x, y, sigma):
    """
    高斯函数
    """
    t = np.exp(-np.linalg.norm(x - y) / (2 * sigma ** 2))
    return t


def sim(i, j):
    """
    计算相似度

    :param i:样本 i
    :param j:样本 j
    :return: 相似度
    """
    return gaussian(i, j, 1)


def get_S_matrix(y_prob):
    """
    计算相似度

    例如：
    样本的预测结果（属于类别0的概率，属于类别1的概率）：
    [[0.8 0.2]
     [0.4 0.6]
     [0.  1. ]]

    得到相似度矩阵：
    [[1.         0.32259073 0.10406478]
     [0.32259073 1.         0.32259073]
     [0.10406478 0.32259073 1.]]

    :param y_prob:预测结果分数
    :return: 相似度矩阵
    """
    mat = np.zeros((len(y_prob), len(y_prob)))
    for i, i_value in enumerate(y_prob):
        for j, j_value in enumerate(y_prob):
            mat[i][j] = sim(i_value, j_value)
    return mat


def get_R_matrix(result):
    """
    将获得的聚类结果转 one-hot 矩阵

    例如：
    聚类结果 [1 2 0 0 1 2 0]
    转成 one-hot 矩阵
    [[0 1 0]
     [0 0 1]
     [1 0 0]
     ...
     [1 0 0]]

    :param result: 聚类结果
    :return:
    """
    mat = np.zeros((len(result), len(np.unique(result))), np.uint8)
    for index, num in enumerate(result):
        mat[index][num] = 1

    return mat
