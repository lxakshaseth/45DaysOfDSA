class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows==1) return s;
        int row=0,i=0;
        bool direction=1; //1 means top to down
        vector<string> zigzag(numRows);
        while(true){
            if(direction){
                while(i<s.size() && row<numRows){
                    zigzag[row++].push_back(s[i++]);
                    // row++;
                    // i++;
                }
                row=numRows-2;
            }
            else{
                while(row>=0 && i<s.size()){
                    zigzag[row--].push_back(s[i++]);
                }
                row=1;
            }
            if(i>=s.size()) break;
            direction=!direction;
        }
        string ans="";
        for(string i:zigzag){
            ans+=i;
        }
        return ans;
    }
};