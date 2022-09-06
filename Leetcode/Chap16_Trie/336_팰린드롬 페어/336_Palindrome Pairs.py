    def palindromePairs(self, words):
        result = []
        root = {}  # use dict instead of a TrieNode class to save space
        for i, word in enumerate(words):
            curr = root
            for idx, ch in enumerate(word):
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
                tmp = word[idx+1:]
                if tmp and self.ispalin(tmp):
                    # keep the idx of word if the suffix of the word after current position is palin
                    curr.setdefault("palin", []).append(i)
            curr["word_idx"] = i  # keep idx of word when reach the end: 몇 번째 단어였는지 트리의 가장 끝에 idx표시

        # 팰린드롬 체크 후 출력
        for j, word in enumerate(words):  # start searching reverse of each word in the Trie
            w = word[::-1]
            curr = root
            fail = False

            for idx, ch in enumerate(w):
                if ch not in curr:
                    fail = True
                    break

                curr = curr[ch]
                # if current node is the end of some word, check whether the suffix of reverse word is palin
                i = curr.get("word_idx")
                if i is not None and i != j and self.ispalin(w[idx+1:]):
                    result.append([i, j])

            if not fail and "palin" in curr:
                result.extend([i, j] for i in curr["palin"] if i != j)

        # "" 예외처리
        if "" in words:  # check for "" case
            idx = words.index("")
            # 공백문자는 원래 팰린드롬인 단어라면 좌우 어디에 붙여도 팰린드롬이니 해당 처리를 해준다
            result.extend(reduce(lambda x, y: x + y, ([[i, idx], [idx, i]] for i, w in enumerate(words) if w and self.ispalin(w))))
        return result
    
    

# # 시간 초과
# # 트라이를 저장할 노드
# class TrieNode:
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)
#         self.word_id = -1
#         self.palindrome_word_ids = []
    
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     @staticmethod
#     def is_palindrome(word: str) -> bool:
#         return word[::] == word[::-1]
    
#     # 단어 삽입
#     def insert(self, index, word) -> None:
#         node = self.root
#         for i, char in enumerate(reversed(word)):
#             if self.is_palindrome(word[0:len(word)-i]):
#                 node.palindrome_word_ids.append(index)
#             node = node.children[char]
#         node.word_id = index
    
#     def search(self, index, word) -> List[List[int]]:
#         result = []
#         node = self.root
        
#         while word:
#             # 판별 로직
#             if node.word_id >= 0:
#                 if self.is_palindrome(word):
#                     result.append([index, node.word_id])
#                 if not word[0] in node.children:
#                     return result
#                 node = node.children[word[0]]
#                 word = word[1:]
                
#         # 판별 로직
#         if node.word_id >= 0 and node.word_id != index:
#             result.append([index, node.word_id])
            
#         # 판별 로직
#         for palindrome_word_id in node.palindrome_word_ids:
#             result.append([index, palindrome_word_id])
        
#         return result

# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         trie = Trie()
        
#         for i, word in enumerate(words):
#             trie.insert(i, word)
        
#         results = []
#         for i, word in enumerate(words):
#             results.extend(trie.search(i, word))
        
#         return results