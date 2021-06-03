<template>
    <transition mode="out-in" enter-active-class="animate__animated animate__fadeIn" leave-active-class="animate__animated animate__fadeOut">
        <a class="navbar-item">
            <span class="icon">
                <slot>
                    <i class="fab fa-google"></i>
                </slot>
            </span>
        </a>
    </transition>
</template>