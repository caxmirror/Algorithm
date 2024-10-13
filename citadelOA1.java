import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



class Result {
    /*
     * Complete the 'getMaximumThroughput' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY throughput
     *  2. INTEGER_ARRAY scaling_cost
     *  3. INTEGER budget
     */

    public static int getMaximumThroughput(List<Integer> throughput, List<Integer> scaling_cost, int budget) {
        
        // heap to continuously modify the min
        PriorityQueue<int []> minheap = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        
        // sort asc
        for (int i = 0; i < throughput.size(); i++){
            
            //total, per, cost
            int[] list = {throughput.get(i), throughput.get(i), scaling_cost.get(i)}; 
            minheap.add(list); 
        }
        
        // create a new heap to store the scaled version, find out the bottleneck
        int consume = 0;
        while (!minheap.isEmpty()) {
            
            int[] list1 = minheap.poll();
            int total = list1[0];
            int per = list1[1];
            int cost = list1[2];
            if (consume + cost <= budget){ 
                consume += cost;
                list1[0] += list1[1]; //update throughput
                minheap.add(list1);
            }
            else{
                return list1[0];
            }
            
            
            
        }
        
        return 0;
        
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int throughputCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> throughput = IntStream.range(0, throughputCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .map(String::trim)
            .map(Integer::parseInt)
            .collect(toList());

        int scaling_costCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> scaling_cost = IntStream.range(0, scaling_costCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .map(String::trim)
            .map(Integer::parseInt)
            .collect(toList());

        int budget = Integer.parseInt(bufferedReader.readLine().trim());

        int result = Result.getMaximumThroughput(throughput, scaling_cost, budget);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
