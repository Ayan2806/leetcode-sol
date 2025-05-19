class Solution {
    public int[] findArray(int[] pref) {
      int n=pref.length;
      for(int itr=n-1;itr>0;itr--){
        pref[itr]=pref[itr]^pref[itr-1];
      }  
      return pref;
    }
}