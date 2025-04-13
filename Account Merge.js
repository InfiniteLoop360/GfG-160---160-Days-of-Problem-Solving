class Solution {
    /**
    * @param number n
    * @param string[][] accounts

    * @returns string[][]
    */
    accountsMerge(accounts) {
        const graph = new Map();
        const emailToName = new Map();
        
        for (let account of accounts){
            const name = account[0];
            const firstEmail = account[1];
            
            for (let i = 1; i < account.length; i++){
                const email = account[i];
                
                emailToName.set(email, name);
                
                if (!graph.has(email)) graph.set(email, []);
                if (!graph.has(firstEmail)) graph.set(firstEmail, []);
                
                graph.get(email).push(firstEmail);
                graph.get(firstEmail).push(email);
            }
        }
        
        const visited = new Set();
        const result = [];
        
        const dfs = (email, component) => {
            visited.add(email);
            component.push(email);
            for (let neighbor of graph.get(email)){
                if (!visited.has(neighbor)){
                    dfs(neighbor, component);
                }
            }
        };
        
        for (let email of graph.keys()){
            if(!visited.has(email)){
                const component = [];
                dfs(email, component);
                component.sort();
                component.unshift(emailToName.get(email));
                result.push(component);
            }
        }
        
        return result;
    }
}
