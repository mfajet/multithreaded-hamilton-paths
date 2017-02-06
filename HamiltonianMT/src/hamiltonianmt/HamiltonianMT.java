/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hamiltonianmt;

import java.util.ArrayList;
import java.util.Stack;

/**
 *
 * @author mfajet
 */
public class HamiltonianMT {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
//# b----c
//# | \/ |
//# | /\ |
//# a    d
        Graph g = new Graph();
        g.addNode('a', new Character[] {'b','c'});
        g.addNode('b', new Character[] {'a','c','d'});
        g.addNode('c', new Character[] {'a','b','d'});
        g.addNode('d', new Character[] {'b','c'});
        
        NonMulti test = new NonMulti();
        for(Stack<Character> a : test.findAllHamiltonianPaths(g)){
            System.out.println(a.toString());
        }
        
    }
    
}
