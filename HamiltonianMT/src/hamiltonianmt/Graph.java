/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hamiltonianmt;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Set;

/**
 *
 * @author mfajet
 */
public class Graph {
    private HashMap<Character,ArrayList<Character>> graph;

    public Graph() {
        graph = new HashMap<>();
    }

    public HashMap<Character,ArrayList<Character>> getGraph(){
        return graph;
    }
    
    public int getLength(){
        return graph.size();
    }
    
    public ArrayList<Character> getAdjVert(char c){
        return graph.get(c);
    }
    
    public Set<Character> getKeys(){
        return graph.keySet();
    }
    
    public void addNode(char c, ArrayList<Character> edges){
        graph.put(c, edges);
    }
    
    public void addNode(char c, Character[] edges){
        ArrayList<Character> l =  new ArrayList<>(Arrays.asList(edges));
        graph.put(c,l);
    }
}
