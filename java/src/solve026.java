import java.util.*;

/*
 * programmers 코딩테스트 입문
 * 순서쌍의 개수
*/

public class solve026{
	
	public static int solution(int n) {
		ArrayList<Integer> xy = new ArrayList<Integer>();		
		System.out.println(Math.sqrt(n));
        for (int i=1; i <= Math.sqrt(n); i++) {
        	if (n % i == 0) {
        		System.out.println(i);
        		if (i != Math.sqrt(n)) {
        			xy.add(i);
        			xy.add(n/i);        			
        		} else xy.add(i);
        	}
        }        
        System.out.println(xy);
        return xy.size();
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
//    	int[] inPut = {30, 10, 23, 6, 100};
    	int inPut = 100;
    	int answer = solution(inPut);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
    }
}
