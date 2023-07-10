import express, { Express, Router, Request, Response } from "express";
import axios from "axios";

const app: Express = express();
app.use('*',(req,res,next)=>{
  
})
const router: Router = express.Router();

app.use("/api", router);

router.get("/list", async (req: Request, res: Response) => {
  const result = await axios.post("https://api.uomg.com/api/rand.qinghua");
  res.json({
    data: result.data,
  });
});

router.get("/lovetalk", async (req: Request, res: Response) => {
  const result = await axios.post("https://api.uomg.com/api/rand.qinghua");
  res.json({
    data: result.data,
  });
});

app.listen(3333, () => {
  console.log("success server http://localhost:3333");
});
