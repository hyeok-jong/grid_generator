batch_size_s=(512 1024)
optimizer_s=('sgd' 'adam')
learning_rate_s=(0.001 0.0001)
model_s=('vit' 'resnet')

start_time=$SECONDS
total_n=16
current_n=0

for model_i in "${model_s[@]}"; do
    for learning_rate_i in "${learning_rate_s[@]}"; do
        for optimizer_i in "${optimizer_s[@]}"; do
            for batch_size_i in "${batch_size_s[@]}"; do
                
                
                current_time=$(date +%T)
                elapsed_time=$((SECONDS - start_time))
                hours=$((elapsed_time / 3600))
                minutes=$(( (elapsed_time % 3600) / 60))
                seconds=$((elapsed_time % 60))
                current_iter=$((current_iter + 1))
                
                echo "Current Time: $current_time"
                echo "Elapsed Time: $hours hour(s) $minutes minute(s) $seconds second(s)"
                echo "Progress: $current_n / $total_n"
                
                CUDA_VISIBLE_DEVICES="0" \
                python train.py \
                --batch_size "${batch_size_i}" \
                --optimizer "${optimizer_i}" \
                --learning_rate "${learning_rate_i}" \
                --model "${model_i}"
            done
        done
    done
done