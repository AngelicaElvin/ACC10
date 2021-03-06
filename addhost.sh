#!/bin/bash

#$(source SNIC2018_10-30-openrc.sh)
$(touch novashow.txt)
$(touch ip.txt)
$(nova show KarinSW > novashow.txt)
$(cat novashow.txt | grep "SNIC" | cut -d " " -f9 > ip.txt)

# insert/update hosts entry
ip_address="$(<ip.txt)"
host_name="sparkworker"
# find existing instances in the host file and save the line numbers
matches_in_hosts="$(grep -n $host_name /etc/hosts | cut -f1 -d:)"
host_entry="${ip_address} ${host_name}"

#echo "Please enter your password if requested."

if [ ! -z "$matches_in_hosts" ]
then
    echo "Updating existing hosts entry."
    # iterate over the line numbers on which matches were found
    while read -r line_number; do
        # replace the text of each line with the desired host entry
        sudo sed -i '' "${line_number}s/.*/${host_entry} /" /etc/hosts
    done <<< "$matches_in_hosts"
else
    echo "Adding new hosts entry."
    echo "$host_entry" | sudo tee -a /etc/hosts > /dev/null
fi

#$(openstack keypair show --public-key KarinSW > pub_key.txt)
