# Approach 1
# Mostly Manual parsing
# O(N), O(N)
class Solution:
    def reverseWords(self, s: str) -> str:
        currWord, words = "", list()
        for i in range(len(s)):
            if s[i] == " ":
                if currWord == "":
                    continue
                words.append(currWord)
                currWord = ""
            else:
                currWord += s[i]
        if currWord != "":
            words.append(currWord)

        n = len(words)
        for i in range(0, (n)//2):
            words[i], words[n-i-1] = words[n-i-1], words[i]
        return ' '.join(words)

# Approach 2
# String Inbuild functions
# O(N), O(N)
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        n = len(words)
        for i in range(0, n//2):
            words[i], words[n-i-1] = words[n-i-1], words[i]
        return ' '.join(words)


# Approach 3 - Inplace
# O(N), O(1)
# While this cannot be done in golang an python, other languages can.
"""
class Solution {
public:
    string reverseWords(string s) {
        reverse(s.begin(), s.end());

        int i = 0, j = 0, n = s.size(), lastIndex = 0;

        while(j < n){
            // Find the starting index of the word: Skipping empty spaces before the word.
            while(j < n && s[j] == ' ') j++;

            int startIndex = i;

            // Store the complete word... :
            while(j < n && s[j] != ' '){
                s[i] = s[j];
                i++;
                j++;
                lastIndex = i;
            }

            // Reverse the word
            reverse(s.begin() + startIndex, s.begin() + lastIndex);
            s[i] = ' '; // after every word we need space [" "]
            i++;
        }

        // Resize the string to the last index of the last word: to avoid empty spaces at the end.
        s.resize(lastIndex);
        return s;
    }
};
"""