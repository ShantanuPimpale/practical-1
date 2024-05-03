const express=require('express')
const mongoose=require('mongoose')

const app=express();
app.use(express.json());

//connecting to Mongodb
async function ConnectDB(){
    try{
        const connection=await mongoose.connect('mongodb+srv://Mayuri:Mayuri24@cluster0.rdnwxxx.mongodb.net/ass3b',
        {   
            useNewUrlParser:true,
            useUnifiedTopology:true
        })
        console.log("Connected To MongoDB Successfully!!")
    }
    catch(error)
    {
        console.log("Error in Connecting to MongoDB ",error)
    }
}

//CURD Operations:
//Operation1:Create
//creating Scehema in MongoDb

const schema=new mongoose.Schema({
    Name:String,
    Surname:String,
    Email:String,
    Age:Number
})

const User=mongoose.model("Profile",schema)

//Adding user to collection

app.post("/adduser",async(req,res)=>{
    try{
        const data=new User(req.body);
        await data.save();
        res.status(201).json({message:"Data Added Successfully",user:data})
    }
    catch(error){
        res.status(500).json({error:"Error While Adding Data to Collection"})
    }
})

//Retrive/read data from collection

app.get("/getuser",async(req,res)=>{
    try
    {
        const read=await User.find();
        res.status(201).json({data:read});
    }
    catch(error)
    {
        res.status(501).json({error:"Error While Fetching Data from Collection"})
    }
})

//Update the User in collection

app.put("/updateuser/:id",async(req,res)=>{
    try
    {
        const userid=req.params.id;
        const updatebody=req.body;
        const update=await User.findByIdAndUpdate(userid,updatebody,{new:true});
        res.status(200).json({message:"Updated Data in Collection Successfully!!"})
    }
    catch(error)
    {
        res.status(500).json({error:"Error in Updating Data!!"})
    }
})

//Deleting user from Collection 

app.delete("/deleteuser/:id",async(req,res)=>{
    try{
        const userid=req.params.id;
        const deleteuser=await User.findByIdAndDelete(userid);
        res.status(200).json({message:"Deleted Data from Collection Successfully!!"})
    }
    catch(error)
    {
        res.status(500).json({error:"Error in Deleting Data!!"})
    }
})

ConnectDB();