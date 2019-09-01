class Solution {
    // Time: O(nlogk)
    // Space :O(k)
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Integer> set = new TreeSet<>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            Integer ceil = set.ceiling(nums[i]); // O(logk)
            Integer floor = set.floor(nums[i]); // O(logk)
            if (ceil != null && ceil - nums[i] <= t && ceil -nums[i] >= 0 || floor != null && Math.abs(floor - nums[i]) <= t && nums[i] - floor >= 0) return true;
            set.add(nums[i]);
            if (set.size() > k) set.remove(nums[i - k]);
        }
        return false;
    }
}
