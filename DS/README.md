# <center> 数据结构与算法 </center> #

## <center> 线性结构 </center> ##
### 线性表的实现 ###
### 栈 ###
### 队列 ###
### 串 ###
### 数组和广义表 ###

## <center> 树型结构 </center> ##

### 树的实现 ###
+ 链式实现
+ 线性表实现——一般只用于完全二叉树
### 二叉树的遍历 ###
+ 递归遍历
  + 前序遍历
  + 中序遍历
  + 后序遍历
+ 线索化二叉树
  + 前/中/后序遍历线索二叉树
### 树 ###
n叉树
Knuth transform
二项树
跳表

### 优先队列 ###
+ 优先队列的实现
  + 多重队列(Multiple Queues)
  + 二叉平衡树(以AVL树为例，AVL Trees)
  + 堆(heap)
+ 堆的分类
  + 小顶堆/大顶堆
  + d-堆
  + *左倾堆(Leftist heap)
  + *斜堆(skew heap)
  + *二叉堆(Binomial heap)
  + *斐波那契堆(Fibonacci heap)
  + **Bi-parental heaps

### 查找树 ###

## <center> 集合结构 </center> ## 

### 哈希表(Hash Map) ###
+ 设计哈希函数
+ 解决冲突
  + 链地址法(Separate Chaining)
  + 开放寻址法(Open Addressing)
    + 线性探测法(Linear Probing)
    + 二次探测法(Quadratic Probing)
    + 再散列法(Double Hashing)
### 并查集(Disjoint Set) ###
+ 并查集的实现
+ 路径压缩算法
  
## <center> 图结构 </center> ##

### 图的实现 ###
+ 邻接矩阵(Adjacency Matrix)
+ 邻接表(Adjacency List)
+ *关联矩阵(Incidence Matrix)
### 图的遍历和应用 ###
+ 深度优先搜索(Depth-first Search)
  + 计算连通分支数
+ 广度优先搜索(Breadth-first Search)
  + 计算连通分支数
  + 在无权图中计算一点到其他所有点的距离
  + 判断一个图是否为二部图
### 图的算法 ###
+ <details><summary>拓扑排序(Topological Sort)</summary>
    空间复杂度为O(V),时间复杂度与图的实现有关，邻接矩阵下为O(V^2)，邻接表下为O(V + E).由于一个图为有向无环图当且仅当该图有一个拓扑排序序列，因此判断一个图是否有环的时间复杂度也为O(V + E).  
    把所有零入度顶点加入队列，每次把队首顶点出队，且在图中删除该顶点，把新生成的零入度顶点入队，直到图空.
    </details>
+ <details><summary>关键路径(Critical Paths)</summary>
  关键路径指在一个带权的有向无环图中总的权值最大的路径，期中分为AOV(activities on vertices,也就是顶点带权而边不带)和AOE(activities on edges,也就是边带权而顶点不带).  
  关键路径算法的控制流程和拓扑排序完全一样，不同的是每次在图中删除一个顶点时都要更新所有与该顶点关联的顶点的Critical time，注意每个顶点(或边)的Task time是给定固定的。  
  时间复杂度和空间复杂度都与拓扑排序一致.
  </details>
+ 最小生成树(Minimum Spaning Tree)  
  最小生成树：一个无向图的生成图（只少边不少点）中所有边权值和（或者称为图的权）最小的那个图（可以证明这一定是一个树，所以也成为最小生成树）
  + <details><summary>Prim’s Algorithm</summary>
    prim算法的空间复杂度为O(V)，时间复杂度根据内部实现的不同有所不同，最基础的prim算法中，直接遍历所有未被遍历的节点更新dis，这种实现的时间复杂度为O(V^2),如果用堆维护所有节点的dis，每次更新dis都可以直接找到所有与u相连的v而不用遍历，则时间复杂度可以下降到O(E*ln(V))，还可以用斐波那契堆进一步优化成O(E + V * ln(V))
    1. 任取图中一点u，设置dis(u)=0，其他节点的dis都为正无穷。
    2. 对于与u关联的每一个未被遍历到的节点v，更新**dis(v) = min{dis(v), W(u, v)}**，若dis(v)成功被更新，则把v节点的父亲节点设置为u，然后把节点u设置为已遍历。
    3. 在所有未被遍历节点中找到dis最小的节点设置为u，重复步骤2直到图中所有节点都已经被遍历，即可得到最小生成树。  
    </details>
  + <details><summary>Kruskal’s Algorithm</summary>
    Kruskal算法的空间复杂度为O(E)，时间复杂度为O(E * ln(E))，关键是注意使用并查集来完成是否构成环的操作，如果不使用并查集，就要通过遍历操作判断是否有环，这时时间复杂度就变成O(V*E)
    1. 对图中的每条边按照权重从小到大排序，把图中的每一个顶点都设置成一个单独的集合
    2. 按照边权从小到大遍历边，首先判断这条边的两个顶点是否属于同一个集合，如果不属于同一个集合就把两个集合合并成同一个（这个操做由并查集完成）并且把这条边加入生成树中。如果属于同一个集合久跳过这条边遍历下一个
    3. 当最小生成树中已经加入了V - 1条边时就可以提前停止算法。
    </details>
  + *Boruvka’s Algorithm 
+ 最短路径问题(Shortest Path Problems)  
  求一个图中从一个点开始到其他所有顶点的最短路径（一定是树状的）.   
  + <details><summary>Dijkstra’s Algorithm</summary>
    解决单源最短路径问题，不允许有负边，有向图和无向图通用  
    Dijkstra算法和Prim算法几乎一样，差别是，在Prim算法中的dis指的是节点与最小生成树的距离，更新公式是**dis(v) = min{dis(v), W(u, v)}**，而在Dijkstra算法中dis指的是节点与指定初始节点之间的距离，更新公式是 **dis(v) = min{dis(v), dis(u) + W(u, v)}** ,除此之外没有任何差别，空间复杂度为O(V)，时间复杂度为O(E * ln(V))
    </details>
  + <details><summary>Bellman-Ford’s Algorithm</summary>
    解决单源最短路径问题，允许有负边不允许负回路，有负边时不能是无向图
    对于有V个节点的图，循环V-1遍如下操作：对于图中每一条边(u,v)，做松弛操作dis(v) = min{dis(v), dis(u) + W(u, v)}，检测负回路的方法：在做完V遍操作后，理论上一定已经找到了最短路径树，这时再循环一边操作不应该有任何一个顶点长度被更新，如果有，就说明有负回路。  
    Bellman-ford算法的空间复杂度为O(1)，但是时间复杂度很高，为O(V * E)  
    Bellman-ford和Dijkstra的比较：后者只更新跟前一个被遍历顶点关联的其他未被遍历顶点，然后还要想办法取出其中的最小值。而前者不关心这些问题，只重复V - 1遍一样的操作  
    </details>
  + <details><summary>Floyd-Warshall’s Algorithm</summary>
    解决图中任两点最短路径问题，允许有负边不允许有负回路，有负边时不能是无向图  
    </details>
  + *A-star Algorithm
+ *网络流问题(Network Flow Problems)
  + Ford-Fulkerson’s Algorithm
  + Edmonds-Karp’s Algorithm
  
## <center> 排序 </center> ##

### 内部排序 ###
+ 平均时间复杂度O(n^2)
  + 直接插入排序 / 二分插入排序(Insertion sort)
  + 选择排序(Selection sort)
  + 冒泡排序(Bubble sort)
+ 平均时间复杂度O(n*ln(n))
  + 堆排序(Heap sort)
  + 快速排序(Quick sort)
  + 归并排序(Merge sort)
+ 平均时间复杂度O(n)
  + 桶排序(Bucket sort)
  + 基数排序(Radix sort)
+ 其他平均时间复杂度
  + 希尔排序(Shell sort)
  + 猴子排序(Bogo sort)
  + 猴子排序变种(Bozo sort)
### 外部排序(External sort) ###
+ 多路归并排序
### 排序算法性质表（考研） ###
