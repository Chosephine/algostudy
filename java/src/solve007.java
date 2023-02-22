import java.util.ArrayList;
import java.util.Arrays;

/*
 * programmers 코딩테스트 입문
 * 짝수는 싫어요
*/

public class solve007{
	

	public static int[] solution(int n) {
        int[] answer = new int[(n + 1)/2];
        
        for (int i=1 ; i<=n ; i++) {
        	if (i % 2 == 1) {
        		answer[i / 2] = i;
        	}
        }
        return answer;
    }

// ArrayList로도 가능!
//	public static ArrayList<Integer> solution(int n) {
//        ArrayList<Integer> answer = new ArrayList<Integer>();
//
//        for(int i=1; i<=n; i++){
//          if(i%2 != 0) {
//              answer.add(i);
//          } 
//        }
//
//        return answer;
//    }
    
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int inPut = 15;
    	int[] answer = solution(inPut);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(Arrays.toString(answer));
//    	System.out.println(answer);
    	
    }
}
