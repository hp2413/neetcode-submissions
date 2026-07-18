class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1arr = [0] * 26
        s2arr = [0] * 26

        for i in range(len(s1)):
            s1arr[ord(s1[i]) - ord('a')] += 1
            s2arr[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2) - len(s1)):
            if self.matches(s1arr, s2arr):
                return True
            s2arr[ord(s2[i + len(s1)]) - ord('a')] += 1
            s2arr[ord(s2[i]) - ord('a')] -= 1

        return self.matches(s1arr, s2arr)

    def matches(self, s1arr, s2arr) -> bool:
        return s1arr == s2arr            
            
            

# public class Solution {
#     public boolean checkInclusion(String s1, String s2) {
#         if (s1.length() > s2.length())
#             return false;
#         int[] s1arr = new int[26];
#         int[] s2arr = new int[26];
#         for (int i = 0; i < s1.length(); i++) {
#             s1arr[s1.charAt(i) - 'a']++;
#             s2arr[s2.charAt(i) - 'a']++;
#         }
#         for (int i = 0; i < s2.length() - s1.length(); i++) {
#             if (matches(s1arr, s2arr))
#                 return true;
#             s2arr[s2.charAt(i + s1.length()) - 'a']++;
#             s2arr[s2.charAt(i) - 'a']--;
#         }
#         return matches(s1arr, s2arr);
#     }
    
#     public boolean matches(int[] s1arr, int[] s2arr) {
#         for (int i = 0; i < 26; i++) {
#             if (s1arr[i] != s2arr[i])
#                 return false;
#         }
#         return true;
#     }
# }