#! /bin/sh
#関数の目的 100までの整数値に対して、FizzBuzzの結果を返す。
#使用方法 第1引数と、第2引数にFizzBuzzの結果を知りたい数字を指定する。
#使用例 3と5のFizzBuzz結果を取得する。
#       FIZZ_BUZZ 3 5 
#正常 0
#異常 1

function FIZZ_BUZZ () {
i=1
x=$1
y=$2

#引数の数をチェック
if [ $# -ne 2 ]; then
  echo "指定された引数は$#個です。" 1>&2
  echo "実行するには2個の引数が必要です。" 1>&2
  exit 1
fi

a=1

#引数の内容をチェック
for z in "$@"
do

expr ${z} + 1 > /dev/null 2>&1
rc=$?
  if [ $rc -lt 2 ]; then
     :
  else
     case "$a" in
     1 ) echo "第1引数が数字かどうかを確認してください。";;
     2 ) echo "第2引数が数字かどうかを確認してください。";;
    esac     
    exit 1
fi
  a=$((a+1))

done

while :
do
  if [ $i -eq 101 ]; then
    break
  fi

  j=$((i%x))
  k=$((i%y))

  if [ $j -eq 0 ] && [ $k -eq 0 ]; then
    echo "FizzBuzz"  
  elif [ $j -eq 0 ]; then
    echo "Fizz"
  elif [ $k -eq 0 ]; then
    echo "Buzz"
  else
    echo $i
  fi

  i=$((i+1))
done

}
