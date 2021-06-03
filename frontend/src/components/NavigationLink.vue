<template>
    <router-link :to="to" class="columns button has-background-link has-text-light is-text">
        <div class="column">
            <slot name="col1">
                <span class="icon">
                    <i class="fas fa-arrow-circle-left"></i>
                </span>
            </slot>
        </div>
        <div class="column">
            <slot name="col2">
                <span>
                    Back to home
                </span>
            </slot>
        </div>
        
    </router-link>
</template>

<script>
export default {
    props: {
        to: {
            type: String,
            required: true
        }
    }
}
</script>