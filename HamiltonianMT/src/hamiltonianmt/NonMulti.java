/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hamiltonianmt;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Stack;

/**
 *
 * @author mfajet
 */
public class NonMulti {
    
    public ArrayList<Stack<Character>> findPathsFromV(Graph g, char v){
            char start = v;
            int n = g.getLength();
            ArrayList<Stack<Character>> paths = new ArrayList<>();
            Stack<Character> path = new Stack<>();
            path.add(v);
            HashMap<Character, Integer> used = new HashMap<>();
            for(Character vertex : g.getKeys()){
                used.put(vertex, 0);
            }
            used.put(v,1);
            HashMap<Character, Integer> countHash = new HashMap<>();
            for(Character vertex : g.getKeys()){
                countHash.put(vertex, 0);
            }
            while(countHash.get(v) < g.getAdjVert(v).size() || (v != start)){
                if (v!=start && countHash.get(v) >= g.getAdjVert(v).size()){
                    v= path.pop();
                    countHash.put(v,0);
                    used.put(v,0);
                    v=path.peek();
                }else{
                    char vert = g.getAdjVert(v).get(countHash.get(v));
                    if(path.size()==n){
                        paths.add((Stack<Character>) path.clone());
                        countHash.put(v,0);
                        used.put(v,0);
                        path.pop();
                        v = path.peek();
                    }else if(used.get(vert)==0){
                        used.put(vert,1);
                        path.push(vert);
                        int i = countHash.get(v) + 1;
                        countHash.put(v,i);
                        v = vert;
                    }else{
                        int i = countHash.get(v) + 1;
                        countHash.put(v,i);                    
                    }
                }
            }
            return paths;
            
    }
    
    public ArrayList<Stack<Character>> findAllHamiltonianPaths(Graph g){
        ArrayList<Stack<Character>> allPaths = new ArrayList<>();
        for(char v : g.getKeys()){
            ArrayList<Stack<Character>> somePaths = findPathsFromV(g,v);
            for(Stack<Character> s : somePaths){
                allPaths.add(s);
            }
        }
        return allPaths;
    }
    
}
