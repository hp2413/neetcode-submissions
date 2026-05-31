class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> hm = new HashMap<>();
        for(char ch: s.toCharArray()){
            hm.put(ch, hm.getOrDefault(ch, 0)+1);
        }
        for(char ch: t.toCharArray()){
            if(!hm.containsKey(ch)) return false;
            hm.put(ch, hm.get(ch)-1);
        }
        for(char key : hm.keySet()){
            if(hm.get(key) != 0) return false;
        }
        return true;
    }
}
