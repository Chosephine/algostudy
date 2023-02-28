import java.util.ArrayList;
import java.util.Arrays;

/*
 * programmers 코딩테스트 입문
 * 배열 뒤집기
*/

public class solve015{
	
	public static ArrayList<Integer> solution(int[] num_list) {
		
		// ArrayList 사용해보기 :>
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        for (int num : num_list) {
        	answer.add(0, num);
        }
        
        return answer;
    }

    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int[] inPut = {1, 0, 1, 1, 1, 3, 5};
//    	int people = 12;
    	ArrayList<Integer> answer = solution(inPut);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
//    	System.out.println(answer);
    }
}
