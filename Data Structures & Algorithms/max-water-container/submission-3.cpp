class Solution {
public:
    int maxArea(vector<int>& heights) {
        int a = 0;
        int b = heights.size() - 1;
        int maxArea = (b-a) * min(heights[a], heights[b]);
        while (a < b){
            if(heights[a] <= heights[b]){
                a += 1;
            }
            else{
                b -= 1;
            }
            int temp = (b-a) * min(heights[a], heights[b]);
            maxArea = max(maxArea, temp);

        }
        return maxArea;
    }
};
