<template>
    <div class="hero-body">
        <slot>
            <transition mode="out-in" enter-active-class="animate__animated animate__zoomIn" leave-active-class="animate__animated animate__zoomOut">
                <router-view></router-view>
            </transition>
        </slot>
    </div>
</template>