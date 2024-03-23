var updateBtns  = document.getElementsByClassName('update-cart')
for (var i=0;i<updateBtns.length;i++)
{
    updateBtns[i].addEventListener('click',function()
    {
        var productId   = this.dataset.product
        var action  =   this.dataset.action
        console.log('poductId:',productId,'action:',action)
        console.log('USER:',user)
        if(user === 'AnonymousUser')
        {
            console.log('Not Logged In')
        }
        else{
            console.log('user is logged in')
        }
    })
}


function updateUserOrder(productId,action)
{
    console.log('user logged in,')
    var url =   '/update_item/'
    fetch(url,{method:'POST',
        headers:{
        'Conetnt-Type':'application/json',
        'X-CSRFToken':csrftoken,
        },
        body:JSON.stringfy({'productId':productId,'action':action})

        })
        .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            console.log('data:'.data)
        })
    }


