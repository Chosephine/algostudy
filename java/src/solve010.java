import java.util.ArrayList;
import java.util.Arrays;

/*
 * programmers 코딩테스트 입문
 * 피자 나눠 먹기 3
*/

public class solve010{
	

	public static int solution(int slice, int n) {

        int answer = n / slice;
        
        if (n % slice != 0) {
        	answer += 1;
        }
        return answer;
    }
    
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int slice = 4;
    	int people = 12;
    	int answer = solution(slice, people);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
//    	System.out.println(answer);
    	
    }
}
