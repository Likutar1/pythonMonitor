#!/bin/bash

echo "--------------------------"
echo "Started script webMonitor.sh"

websites=(
  "https://www.salford.gov.uk abc"
  "https://www.google.com Lucky"
  "https://www.facebook.com Facebook"
  "https://www.fakewebsite_asdlkfjvioervklasddf.com Rubbish"
)

for web in "${websites[@]}"; do
  url=$(echo "$web" | awk '{print $1}')
  keyword=$(echo "$web" | awk '{print $2}')

  echo ""
  date
  echo "Checking $url"

  response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

  echo "Response: $response"

  if [[ "$response" -eq 200 ]]; then
    echo "The site is up."
    if curl -s "$url" | grep -q "$keyword"; then
      echo "Keyword $keyword is found."
    else
      echo "Keyword $keyword was not found."
    fi
  elif [[ "$response" -eq 403 ]]; then
    echo "Access refusal."
  else
    echo "Unsure, please check."
  fi
done
