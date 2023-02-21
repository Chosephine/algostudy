import java.util.Arrays;

/*
 * programmers 코딩테스트 입문
 * 최빈값 구하기
*/

public class solve006{
	

	public static int solution(int[] array) {
        int answer = 0;
        
        // array에 나오는 숫자 갯수를 셀 cnt 배열 초기화
        // array의 원소는 0보다 크거나 같고, 1000보다 작으므로 0~999까지의 값이 나올 수 있음
        int[] cnt = new int[1000];
        
        // array에 나오는 숫자 세기
        for (int num : array) {
        	cnt[num] += 1;
        }
        
        int maxNum = Arrays.stream(cnt).max().getAsInt();
        int maxIndex = -1;
        
        // cnt에서 max값 찾기
        for (int i = 0; i < 1000; i++) {
        	if (cnt[i] == maxNum) {
        		if (maxIndex != -1) {
        			answer = -1;
        			return answer;
        		} else maxIndex = i;
        		
        	}
        }
        answer = maxIndex;
        
        return answer;
    }
    
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int[] inPut = {1, 1, 2, 2};
    	int answer = solution(inPut);
    	System.out.println(answer);
    	
    }
}
