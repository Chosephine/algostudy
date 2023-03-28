
/*
 * programmers 코딩테스트 입문
 * 점의 위치 구하기
*/

public class solve031{

	public static int solution(int[] dot) {
        int x = dot[0];
        int y = dot[1];
        if (x > 0) {
        	if (y > 0) {
        		return 1;        		
        	} else {
        		return 4;
    		} 
        } else {
        	if (y > 0) {
        		return 2;        		
        	} else {
        		return 3;
    		}
        }
        
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int[] inPut = {-7, 9}; 
    	int answer = solution(inPut);
    	System.out.println(answer);
    }
}
