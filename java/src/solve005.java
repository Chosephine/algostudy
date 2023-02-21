import java.util.Arrays;

/*
 * programmers 코딩테스트 입문
 * 중앙값 구하기
*/

public class solve005{
	
	public static int solution(int[] array) {
        int loc = array.length / 2;
        Arrays.sort(array);
        return array[loc];
    }
    
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int[] inPut = {9, -1, 0};
    	int answer = solution(inPut);
    	System.out.println(answer);
    	
    }
}
