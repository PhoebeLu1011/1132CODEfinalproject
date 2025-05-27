# 113-2 Programming Language Final Project 
# Life Explosion Simulator: Final Exam Hell Edition

## 組員:
- <a href="https://github.com/PhoebeLu1011"><img src="https://github.com/PhoebeLu1011.png" width="20"/> @PhoebeLu1011</a>
- <a href="https://github.com/kurakanja"><img src="https://github.com/kurakanja.png" width="20"/> @kurakanja</a>

## 第一次審查連結 : https://youtu.be/SExgqFcxvvw
## 第二次進度追蹤 : https://youtu.be/0_wMfQdEzZ0
## 若程式跑不動  
請手動新增一個.env檔，裡面寫GEMINI_API_KEY=你的google api key  
並且在cmd(命令提示字元)輸入  
pip install flask  
pip install google-generativeai  
pip install python-dotenv  
pip install pygame   
## 動機 
身為大學生的我們，每學期在期末時，必經歷大量作業、考試與專題的壓力，導致爆肝、熬夜與情緒崩潰等現象頻繁發生，俗稱 「期末地獄」。
## 目標
本專題希望遊戲模擬去呈現學生在期末地獄中掙扎的情境，讓使用者放鬆，並達到娛樂效果。

## 遊戲示意圖  
* 主介面
<img src="images/遊戲畫面.png" width="500"/>

* 觸碰教授圖像，觸發情節圖
<img src="images/教授畫面.png" width="500"/>
* 觸碰五次睡覺圖像，觸發情節圖
<img src="code/images/teachertheme/ttheme_sleep.png" width="500"/>
* 觸碰五次喝酒圖像，觸發情節圖
<img src="code/images/teachertheme/ttheme_drink.png" width="500"/>
* 讀書進度達100，成功逃離期末地獄
<img src="code/images/ending/ending_study100.png" width="500"/>  
* 精力值為0，進入頹廢結局
<img src="code/images/ending/ending_energy0.png" width="500"/>  
* 健康值為0，進入送醫結局
<img src="code/images/ending/ending_health0.png" width="500"/>  
* 撞到車，進入車禍結局
<img src="code/images/ending/ending_car.png" width="500"/>  

* 遊戲結束畫面\
| 成功(逃脫期末地獄) | 失敗 |
|--------|------|
| <img src="images/成功最後畫面.png" width="400"/> | <img src="images/失敗最後畫面.png" width="400"/> |

## 使用程式
* PYTHON
* PYGAME
* 作業二-資料視覺化
  
## 遊戲流程
<img src="images/IMAGE1.png" width="500"/>

## 道具介紹

### 各項值選項介紹

* 課業完成度：[█████████░░] 90%
* 健康值：[█████████░░] 90%
* 精力值：[█████████░░] 90%

### 道具介紹

| 道具圖 | 道具名稱 | 說明 |
|--------|------|------|
| <img src="images/讀書.png" width="100"/> | 書 | 課業完成度+10、 精力值-20|
| <img src="images/寫報告.png" width="100"/> | 報告 |課業完成度+10、精力值+5|
| <img src="images/食物.png" width="100"/> | 食物(雞腿) |健康值+5、精力值+5|
| <img src="images/睡覺.png" width="100"/> | 睡覺(枕頭) |健康值+10、精力值+5<br>注意:接觸5次睡覺時會觸發特殊事件(在圖書館睡著)，導致讀書進度-10|
| <img src="images/喝酒.png" width="100"/> | 喝酒(啤酒杯) |健康值-15、精力值+10<br>注意:接觸5次喝酒時會觸發特殊事件(參加酒局，隔天宿醉)，導致健康值-10、課業完成度-10|
| <img src="images/教授.png" width="100"/> | 教授 |稀有!根據四種不同事件，可能使精力值-10~+5、課業完成度-10~+10不等<br>以下為四種不同的事件:<br>1."太好了同學，剛好你來幫我整理這些文件吧!"(被迫幫忙教授):精力值-10<br>2. “同學有哪裡不懂嗎"(和教授討論中):課業完成度+10<br>3."同學你的報告寫得非常好!"(被誇獎了好開心):精力值+5<br>4."同學你來幫忙紀錄一下這場會議好嗎，還有明天順便幫我聯絡，禮拜五的時候也......"(事情突然好多......):精力值-10、課業完成度-10|

### 各項值使用方法說明

1.  各項數值意義 :\
作業完成度  → 破關條件\
精力值 → 體力❤️❤️❤️❤️❤️\
健康值 → (倒數)時間
2.  遊戲方法:\
當作業完成度=100%  → 跳出結局1(all pass，拯救期末成功)\
當作業完成度< 100% → 繼續遊戲\
                  → 當精力值=0%→跳出結局2(救護車出現將玩家送進醫院)\
                  → 當健康值=0%→跳出結局3(有科目被當掉，拯救期末失敗)


