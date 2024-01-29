import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/*
 * 백준 2751 수 정렬하기2
 * https://www.acmicpc.net/problem/2751
*/

public class solve061 {
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 이 문제는 StringBuilder을 사용하지 않으면 시간초과가 난다..!
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		
		// Collections.sort()를 사용하기 위한 ArrayList 자료구조 사용
		// Arrays.sort() 는 최악의 경우 O(n^2)의 시간 복잡도를 가지기 때문에 이 문제에 적합하지 않음
		// Collections.sort() 는 최선, 최악 모두 O(nlogn)을 보장함
		List<Integer> arrList = new ArrayList<Integer>();
		
		for (int i = 0; i < N; i++) {
			
			arrList.add(Integer.parseInt(br.readLine()));
			
		}
		
		
		Collections.sort(arrList);
		
		// 직접 순회하면서 print하면 시간초과
		// for(int value : arrList) {
		// 	
		// 	System.out.println(value);
		// 	
		// }
		
		// sb를 통해 프린트할 결과물을 구성하여야 함 
		for(int value : arrList) {
			sb.append(value).append('\n');
		}
		
		System.out.println(sb);
		
	}
}
