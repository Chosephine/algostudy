import java.util.ArrayList;
import java.util.Arrays;

/*
 * programmers 코딩테스트 입문
 * 피자 나눠 먹기 1
*/

public class solve008{
	

	public static int solution(int n) {
        return (n - 1) / 7 + 1;
    }
    
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int inPut = 15;
    	int answer = solution(inPut);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
//    	System.out.println(answer);
    	
    }
}
