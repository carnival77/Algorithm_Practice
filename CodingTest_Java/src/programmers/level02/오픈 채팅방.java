package programmers.level02.OpenChatRoom;
import java.util.*;

public class OpenChatRoom_carnival77 {
    class Solution {

        StringTokenizer st = new StringTokenizer("");
        HashMap<String,String> ID_Name = new HashMap<>();

        public String[] solution(String[] record) {
            for(int i=record.length-1;i>=0;i--){
                st = new StringTokenizer(record[i]);
                if(st.nextToken().equals("Leave")) {
                    continue;
                }
                String id = st.nextToken();
                String name = st.nextToken();
                if(!ID_Name.containsKey(id)) {
                    ID_Name.put(id,name);
                }
            }
            ArrayList<String> ans = new ArrayList<>();
            String in = "님이 들어왔습니다.";
            String out = "님이 나갔습니다.";

            for(int i=0;i<record.length;i++){
                st = new StringTokenizer(record[i]);
                String s = st.nextToken();
                if(s.equals("Enter")) {
                    ans.add(ID_Name.get(st.nextToken())+in);
                }
                else if(s.equals("Leave")) {
                    ans.add(ID_Name.get(st.nextToken())+out);
                }
            }
            return ans.toArray(new String[ans.size()]);

        }
    }
}
