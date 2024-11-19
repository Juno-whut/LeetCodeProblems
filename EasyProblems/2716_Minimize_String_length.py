class Solution:
    def minimizedStringLength(self, s: str):
        seen = set()
        for i in s:
            seen.add(i)
        return len(seen)

def main():
    s = "cabaabac"
    print(Solution.minimizedStringLength(Solution, s))
    s = 'abcd'
    print(Solution.minimizedStringLength(Solution, s))
    s = 'aa'
    print(Solution.minimizedStringLength(Solution, s))

if __name__ == "__main__":
    main()