# Problem J4: From Prefix to Postfix

operator = ['-', '+']

def postfix(pre):

    if len(pre) == 1:
        return [pre[0]]
    
    if pre[0] in operator:
        if pre[1] in operator:
            if pre[2] not in operator and pre[3] not in operator and pre[4] in operator:
                post = postfix(pre[1:4])
                post += postfix(pre[4:])
                post.append(pre[0])   
            else:                                
                post = postfix(pre[1:-1])
                post.append(pre[-1])
                post.append(pre[0])

        else:
            post = [pre[1]]
            post += postfix(pre[2:])
            post.append(pre[0])

        return post

prefix = input().split()

while prefix[0] != '0':
    post = postfix(prefix)
    print(*post)
    prefix = input().split()
